from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrinterCapabilities(BaseModel):
	bottomMargins: Optional[list[int]] = Field(default=None,alias="bottomMargins",)
	collation: Optional[bool] = Field(default=None,alias="collation",)
	colorModes: Optional[PrintColorMode] = Field(default=None,alias="colorModes",)
	contentTypes: Optional[list[str]] = Field(default=None,alias="contentTypes",)
	copiesPerJob: Optional[IntegerRange] = Field(default=None,alias="copiesPerJob",)
	dpis: Optional[list[int]] = Field(default=None,alias="dpis",)
	duplexModes: Optional[PrintDuplexMode] = Field(default=None,alias="duplexModes",)
	feedOrientations: Optional[PrinterFeedOrientation] = Field(default=None,alias="feedOrientations",)
	finishings: Optional[PrintFinishing] = Field(default=None,alias="finishings",)
	inputBins: Optional[list[str]] = Field(default=None,alias="inputBins",)
	isColorPrintingSupported: Optional[bool] = Field(default=None,alias="isColorPrintingSupported",)
	isPageRangeSupported: Optional[bool] = Field(default=None,alias="isPageRangeSupported",)
	leftMargins: Optional[list[int]] = Field(default=None,alias="leftMargins",)
	mediaColors: Optional[list[str]] = Field(default=None,alias="mediaColors",)
	mediaSizes: Optional[list[str]] = Field(default=None,alias="mediaSizes",)
	mediaTypes: Optional[list[str]] = Field(default=None,alias="mediaTypes",)
	multipageLayouts: Optional[PrintMultipageLayout] = Field(default=None,alias="multipageLayouts",)
	orientations: Optional[PrintOrientation] = Field(default=None,alias="orientations",)
	outputBins: Optional[list[str]] = Field(default=None,alias="outputBins",)
	pagesPerSheet: Optional[list[int]] = Field(default=None,alias="pagesPerSheet",)
	qualities: Optional[PrintQuality] = Field(default=None,alias="qualities",)
	rightMargins: Optional[list[int]] = Field(default=None,alias="rightMargins",)
	scalings: Optional[PrintScaling] = Field(default=None,alias="scalings",)
	supportsFitPdfToPage: Optional[bool] = Field(default=None,alias="supportsFitPdfToPage",)
	topMargins: Optional[list[int]] = Field(default=None,alias="topMargins",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .print_color_mode import PrintColorMode
from .integer_range import IntegerRange
from .print_duplex_mode import PrintDuplexMode
from .printer_feed_orientation import PrinterFeedOrientation
from .print_finishing import PrintFinishing
from .print_multipage_layout import PrintMultipageLayout
from .print_orientation import PrintOrientation
from .print_quality import PrintQuality
from .print_scaling import PrintScaling

