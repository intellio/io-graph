from __future__ import annotations
from enum import StrEnum


class Label(StrEnum):
	title = "title"
	url = "url"
	createdBy = "createdBy"
	lastModifiedBy = "lastModifiedBy"
	authors = "authors"
	createdDateTime = "createdDateTime"
	lastModifiedDateTime = "lastModifiedDateTime"
	fileName = "fileName"
	fileExtension = "fileExtension"

