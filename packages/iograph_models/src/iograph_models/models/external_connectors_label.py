from __future__ import annotations
from enum import Enum


class ExternalConnectorsLabel(Enum):
	title = "title"
	url = "url"
	createdBy = "createdBy"
	lastModifiedBy = "lastModifiedBy"
	authors = "authors"
	createdDateTime = "createdDateTime"
	lastModifiedDateTime = "lastModifiedDateTime"
	fileName = "fileName"
	fileExtension = "fileExtension"
	unknownFutureValue = "unknownFutureValue"
	iconUrl = "iconUrl"

