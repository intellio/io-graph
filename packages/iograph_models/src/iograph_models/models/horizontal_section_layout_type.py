from __future__ import annotations
from enum import StrEnum


class HorizontalSectionLayoutType(StrEnum):
	none = "none"
	oneColumn = "oneColumn"
	twoColumns = "twoColumns"
	threeColumns = "threeColumns"
	oneThirdLeftColumn = "oneThirdLeftColumn"
	oneThirdRightColumn = "oneThirdRightColumn"
	fullWidth = "fullWidth"
	unknownFutureValue = "unknownFutureValue"

