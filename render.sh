#!/usr/bin/env bash
export QUARTO_PYTHON="$(pixi run which python)"
quarto render semantic-drift-tech.qmd
