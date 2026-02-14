"""
CLI for Editing Open-Document Presentations

Add notes to slides or dim texts

Created on 14.02.2026
@author: Mathias Berg Rosendal
         PhD Student at DTU Management (Energy Economics & Modelling)
"""
# ------------------------------- #
#        0. Script Settings       #
# ------------------------------- #

import click
from notes import add_notes_to_slide

# ------------------------------- #
#          1. Functions           #
# ------------------------------- #


# ------------------------------- #
#            2. Main              #
# ------------------------------- #


@click.group()
def main():

    pass


@main.command()
@click.argument("odp_path", type=str)
@click.argument("odp_output_path", type=str)
@click.argument("slide_index", type=int)
@click.argument("notes_text", type=str)
def add_notes(odp_path, odp_output_path, slide_index, notes_text):

    add_notes_to_slide(
        odp_path,
        odp_output_path,
        slide_index=slide_index,
        notes_text=notes_text.split("\\n"),
    )


if __name__ == "__main__":
    main()
