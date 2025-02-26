from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintUsageByUser(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	blackAndWhitePageCount: Optional[int] = Field(default=None,alias="blackAndWhitePageCount",)
	colorPageCount: Optional[int] = Field(default=None,alias="colorPageCount",)
	completedBlackAndWhiteJobCount: Optional[int] = Field(default=None,alias="completedBlackAndWhiteJobCount",)
	completedColorJobCount: Optional[int] = Field(default=None,alias="completedColorJobCount",)
	completedJobCount: Optional[int] = Field(default=None,alias="completedJobCount",)
	doubleSidedSheetCount: Optional[int] = Field(default=None,alias="doubleSidedSheetCount",)
	incompleteJobCount: Optional[int] = Field(default=None,alias="incompleteJobCount",)
	mediaSheetCount: Optional[int] = Field(default=None,alias="mediaSheetCount",)
	pageCount: Optional[int] = Field(default=None,alias="pageCount",)
	singleSidedSheetCount: Optional[int] = Field(default=None,alias="singleSidedSheetCount",)
	usageDate: Optional[str] = Field(default=None,alias="usageDate",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)


