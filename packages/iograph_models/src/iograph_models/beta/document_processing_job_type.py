from __future__ import annotations
from enum import StrEnum


class DocumentProcessingJobType(StrEnum):
	file = "file"
	folder = "folder"
	unknownFutureValue = "unknownFutureValue"

