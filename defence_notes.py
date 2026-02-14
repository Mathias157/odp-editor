"""
PhD Defence Presentation

Corrections to my PhD Defence Presentation

Created on 14.02.2026
@author: Mathias Berg Rosendal
         PhD Student at DTU Management (Energy Economics & Modelling)
"""
# ------------------------------- #
#        0. Script Settings       #
# ------------------------------- #

import click
from notes import batch_add_notes

# ------------------------------- #
#          1. Functions           #
# ------------------------------- #


# ------------------------------- #
#            2. Main              #
# ------------------------------- #


@click.command()
def main():

    presentation = "Defence Presentation.odp"
    odp_output_path = "Defence Presentation I.odp"

    with open("defence_notes.md", "r") as f:
        notes = f.read()

    separate_notes = [note for note in notes.split("## ") if note != ""]

    notes_batch = {}
    for i, note in enumerate(separate_notes):
        print(i, note)
        notes_batch[i] = note.split("\n")

    batch_add_notes(
        presentation,
        odp_output_path,
        notes_batch,
    )


if __name__ == "__main__":
    main()
