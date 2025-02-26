from __future__ import annotations
from enum import Enum


class AutomaticRepliesStatus(Enum):
	disabled = "disabled"
	alwaysEnabled = "alwaysEnabled"
	scheduled = "scheduled"

