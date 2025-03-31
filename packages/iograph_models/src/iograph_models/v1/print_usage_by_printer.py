from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PrintUsageByPrinter(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.printUsageByPrinter"] = Field(alias="@odata.type", default="#microsoft.graph.printUsageByPrinter")
	blackAndWhitePageCount: Optional[int] = Field(alias="blackAndWhitePageCount", default=None,)
	colorPageCount: Optional[int] = Field(alias="colorPageCount", default=None,)
	completedBlackAndWhiteJobCount: Optional[int] = Field(alias="completedBlackAndWhiteJobCount", default=None,)
	completedColorJobCount: Optional[int] = Field(alias="completedColorJobCount", default=None,)
	completedJobCount: Optional[int] = Field(alias="completedJobCount", default=None,)
	doubleSidedSheetCount: Optional[int] = Field(alias="doubleSidedSheetCount", default=None,)
	incompleteJobCount: Optional[int] = Field(alias="incompleteJobCount", default=None,)
	mediaSheetCount: Optional[int] = Field(alias="mediaSheetCount", default=None,)
	pageCount: Optional[int] = Field(alias="pageCount", default=None,)
	singleSidedSheetCount: Optional[int] = Field(alias="singleSidedSheetCount", default=None,)
	usageDate: Optional[str] = Field(alias="usageDate", default=None,)
	printerId: Optional[str] = Field(alias="printerId", default=None,)
	printerName: Optional[str] = Field(alias="printerName", default=None,)

