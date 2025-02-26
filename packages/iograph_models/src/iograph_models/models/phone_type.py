from __future__ import annotations
from enum import Enum


class PhoneType(Enum):
	home = "home"
	business = "business"
	mobile = "mobile"
	other = "other"
	assistant = "assistant"
	homeFax = "homeFax"
	businessFax = "businessFax"
	otherFax = "otherFax"
	pager = "pager"
	radio = "radio"

