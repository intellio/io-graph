from __future__ import annotations
from enum import StrEnum


class SecurityCloudAttachmentVersion(StrEnum):
	latest = "latest"
	recent10 = "recent10"
	recent100 = "recent100"
	all = "all"
	unknownFutureValue = "unknownFutureValue"

