import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import tempfile

NAMESPACES = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "presentation": "urn:oasis:names:tc:opendocument:xmlns:presentation:1.0",
    "draw": "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "svg": "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    "fo": "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
    "style": "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
}

for prefix, uri in NAMESPACES.items():
    ET.register_namespace(prefix, uri)


def add_notes_to_slide(odp_path, output_path, slide_index, notes_text):
    """
    Add speaker notes to a specific slide.

    Args:
        odp_path: Path to input .odp file
        output_path: Path to output .odp file
        slide_index: 0-based slide index
        notes_text: Text content for the notes (can be string or list of paragraphs)
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Extract ODP
        with zipfile.ZipFile(odp_path, "r") as zip_ref:
            zip_ref.extractall(temp_path)

        # Parse content.xml
        content_path = temp_path / "content.xml"
        tree = ET.parse(content_path)
        root = tree.getroot()

        # Find the target slide
        slides = root.findall(".//draw:page", NAMESPACES)
        if slide_index >= len(slides):
            raise ValueError(f"Slide index {slide_index} out of range")

        target_slide = slides[slide_index]

        # Remove existing notes if present
        existing_notes = target_slide.find("presentation:notes", NAMESPACES)
        if existing_notes is not None:
            target_slide.remove(existing_notes)

        # Create notes structure
        notes_element = ET.SubElement(
            target_slide,
            f"{{{NAMESPACES['presentation']}}}notes",
            {f"{{{NAMESPACES['draw']}}}style-name": "dp2"},
        )

        # Add page thumbnail (optional but standard)
        thumbnail = ET.SubElement(
            notes_element,
            f"{{{NAMESPACES['draw']}}}page-thumbnail",
            {
                f"{{{NAMESPACES['draw']}}}style-name": "gr1",
                f"{{{NAMESPACES['draw']}}}layer": "layout",
                f"{{{NAMESPACES['svg']}}}width": "12.768cm",
                f"{{{NAMESPACES['svg']}}}height": "9.576cm",
                f"{{{NAMESPACES['svg']}}}x": "3.629cm",
                f"{{{NAMESPACES['svg']}}}y": "2.257cm",
                f"{{{NAMESPACES['presentation']}}}class": "page",
            },
        )

        # Create text frame for notes
        frame = ET.SubElement(
            notes_element,
            f"{{{NAMESPACES['draw']}}}frame",
            {
                f"{{{NAMESPACES['presentation']}}}style-name": "pr1",
                f"{{{NAMESPACES['draw']}}}layer": "layout",
                f"{{{NAMESPACES['svg']}}}width": "16.79cm",
                f"{{{NAMESPACES['svg']}}}height": "11.303cm",
                f"{{{NAMESPACES['svg']}}}x": "2.098cm",
                f"{{{NAMESPACES['svg']}}}y": "13.362cm",
                f"{{{NAMESPACES['presentation']}}}class": "notes",
                f"{{{NAMESPACES['presentation']}}}placeholder": "true",
            },
        )

        # Create text box
        text_box = ET.SubElement(frame, f"{{{NAMESPACES['draw']}}}text-box")

        # Add text content (support multiple paragraphs)
        if isinstance(notes_text, str):
            notes_text = [notes_text]

        for paragraph in notes_text:
            p = ET.SubElement(text_box, f"{{{NAMESPACES['text']}}}p")
            p.text = paragraph

        # Save modified content.xml
        tree.write(content_path, encoding="utf-8", xml_declaration=True)

        # Repackage as ODP
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zip_out:
            for file_path in temp_path.rglob("*"):
                if file_path.is_file():
                    arcname = file_path.relative_to(temp_path)
                    zip_out.write(file_path, arcname)


def batch_add_notes(odp_path, output_path, notes_config):
    """
    Add notes to multiple slides at once.

    Args:
        notes_config: dict mapping slide index to notes text
        Example: {0: "Notes for slide 1", 1: ["Point 1", "Point 2"]}
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        with zipfile.ZipFile(odp_path, "r") as zip_ref:
            zip_ref.extractall(temp_path)

        content_path = temp_path / "content.xml"
        tree = ET.parse(content_path)
        root = tree.getroot()

        slides = root.findall(".//draw:page", NAMESPACES)

        for slide_index, notes_text in notes_config.items():
            if slide_index >= len(slides):
                print(f"Warning: Slide index {slide_index} out of range, skipping")
                continue

            target_slide = slides[slide_index]

            # Remove existing notes
            existing_notes = target_slide.find("presentation:notes", NAMESPACES)
            if existing_notes is not None:
                target_slide.remove(existing_notes)

            # Create new notes
            notes_element = ET.SubElement(
                target_slide,
                f"{{{NAMESPACES['presentation']}}}notes",
                {f"{{{NAMESPACES['draw']}}}style-name": "dp2"},
            )

            # Add thumbnail
            ET.SubElement(
                notes_element,
                f"{{{NAMESPACES['draw']}}}page-thumbnail",
                {
                    f"{{{NAMESPACES['draw']}}}style-name": "gr1",
                    f"{{{NAMESPACES['draw']}}}layer": "layout",
                    f"{{{NAMESPACES['svg']}}}width": "12.768cm",
                    f"{{{NAMESPACES['svg']}}}height": "9.576cm",
                    f"{{{NAMESPACES['svg']}}}x": "3.629cm",
                    f"{{{NAMESPACES['svg']}}}y": "2.257cm",
                    f"{{{NAMESPACES['presentation']}}}class": "page",
                },
            )

            # Add text frame
            frame = ET.SubElement(
                notes_element,
                f"{{{NAMESPACES['draw']}}}frame",
                {
                    f"{{{NAMESPACES['presentation']}}}style-name": "pr1",
                    f"{{{NAMESPACES['draw']}}}layer": "layout",
                    f"{{{NAMESPACES['svg']}}}width": "16.79cm",
                    f"{{{NAMESPACES['svg']}}}height": "11.303cm",
                    f"{{{NAMESPACES['svg']}}}x": "2.098cm",
                    f"{{{NAMESPACES['svg']}}}y": "13.362cm",
                    f"{{{NAMESPACES['presentation']}}}class": "notes",
                    f"{{{NAMESPACES['presentation']}}}placeholder": "true",
                },
            )

            text_box = ET.SubElement(frame, f"{{{NAMESPACES['draw']}}}text-box")

            if isinstance(notes_text, str):
                notes_text = [notes_text]

            for paragraph in notes_text:
                p = ET.SubElement(text_box, f"{{{NAMESPACES['text']}}}p")
                p.text = paragraph

        tree.write(content_path, encoding="utf-8", xml_declaration=True)

        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zip_out:
            for file_path in temp_path.rglob("*"):
                if file_path.is_file():
                    arcname = file_path.relative_to(temp_path)
                    zip_out.write(file_path, arcname)


if __name__ == "__main__":
    # Example usage
    add_notes_to_slide(
        "presentation.odp",
        "presentation_with_notes.odp",
        slide_index=0,
        notes_text="Remember to emphasize the key benefits here",
    )

    # Or with multiple paragraphs
    add_notes_to_slide(
        "presentation.odp",
        "presentation_with_notes.odp",
        slide_index=1,
        notes_text=[
            "First key point to mention",
            "Second important detail",
            "Don't forget the demo",
        ],
    )

    # Example usage
    notes = {
        0: "Introduction slide - keep it brief, smile!",
        1: ["Market size: $5B", "Growth rate: 25% YoY", "Show enthusiasm"],
        2: "Demo time - make sure the laptop is ready",
        5: ["Mention competitor weaknesses", "Emphasize our unique value prop"],
    }

    batch_add_notes("presentation.odp", "presentation_with_all_notes.odp", notes)
