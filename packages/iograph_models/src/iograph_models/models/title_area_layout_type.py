from __future__ import annotations
from enum import Enum


class TitleAreaLayoutType(Enum):
	imageAndTitle = "imageAndTitle"
	plain = "plain"
	colorBlock = "colorBlock"
	overlap = "overlap"
	unknownFutureValue = "unknownFutureValue"

