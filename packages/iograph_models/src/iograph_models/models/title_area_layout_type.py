from __future__ import annotations
from enum import StrEnum


class TitleAreaLayoutType(StrEnum):
	imageAndTitle = "imageAndTitle"
	plain = "plain"
	colorBlock = "colorBlock"
	overlap = "overlap"
	unknownFutureValue = "unknownFutureValue"

