from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintJobConfiguration(BaseModel):
	collate: Optional[bool] = Field(default=None,alias="collate",)
	colorMode: Optional[PrintColorMode] = Field(default=None,alias="colorMode",)
	copies: Optional[int] = Field(default=None,alias="copies",)
	dpi: Optional[int] = Field(default=None,alias="dpi",)
	duplexMode: Optional[PrintDuplexMode] = Field(default=None,alias="duplexMode",)
	feedOrientation: Optional[PrinterFeedOrientation] = Field(default=None,alias="feedOrientation",)
	finishings: Optional[PrintFinishing] = Field(default=None,alias="finishings",)
	fitPdfToPage: Optional[bool] = Field(default=None,alias="fitPdfToPage",)
	inputBin: Optional[str] = Field(default=None,alias="inputBin",)
	margin: Optional[PrintMargin] = Field(default=None,alias="margin",)
	mediaSize: Optional[str] = Field(default=None,alias="mediaSize",)
	mediaType: Optional[str] = Field(default=None,alias="mediaType",)
	multipageLayout: Optional[PrintMultipageLayout] = Field(default=None,alias="multipageLayout",)
	orientation: Optional[PrintOrientation] = Field(default=None,alias="orientation",)
	outputBin: Optional[str] = Field(default=None,alias="outputBin",)
	pageRanges: list[IntegerRange] = Field(alias="pageRanges",)
	pagesPerSheet: Optional[int] = Field(default=None,alias="pagesPerSheet",)
	quality: Optional[PrintQuality] = Field(default=None,alias="quality",)
	scaling: Optional[PrintScaling] = Field(default=None,alias="scaling",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .print_color_mode import PrintColorMode
from .print_duplex_mode import PrintDuplexMode
from .printer_feed_orientation import PrinterFeedOrientation
from .print_finishing import PrintFinishing
from .print_margin import PrintMargin
from .print_multipage_layout import PrintMultipageLayout
from .print_orientation import PrintOrientation
from .integer_range import IntegerRange
from .print_quality import PrintQuality
from .print_scaling import PrintScaling

