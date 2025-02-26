from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrinterCapabilities(BaseModel):
	bottomMargins: list[Optional[int]] = Field(alias="bottomMargins",)
	collation: Optional[bool] = Field(default=None,alias="collation",)
	colorModes: Optional[PrintColorMode] = Field(default=None,alias="colorModes",)
	contentTypes: list[Optional[str]] = Field(alias="contentTypes",)
	copiesPerJob: Optional[IntegerRange] = Field(default=None,alias="copiesPerJob",)
	dpis: list[Optional[int]] = Field(alias="dpis",)
	duplexModes: Optional[PrintDuplexMode] = Field(default=None,alias="duplexModes",)
	feedOrientations: Optional[PrinterFeedOrientation] = Field(default=None,alias="feedOrientations",)
	finishings: Optional[PrintFinishing] = Field(default=None,alias="finishings",)
	inputBins: list[Optional[str]] = Field(alias="inputBins",)
	isColorPrintingSupported: Optional[bool] = Field(default=None,alias="isColorPrintingSupported",)
	isPageRangeSupported: Optional[bool] = Field(default=None,alias="isPageRangeSupported",)
	leftMargins: list[Optional[int]] = Field(alias="leftMargins",)
	mediaColors: list[Optional[str]] = Field(alias="mediaColors",)
	mediaSizes: list[Optional[str]] = Field(alias="mediaSizes",)
	mediaTypes: list[Optional[str]] = Field(alias="mediaTypes",)
	multipageLayouts: Optional[PrintMultipageLayout] = Field(default=None,alias="multipageLayouts",)
	orientations: Optional[PrintOrientation] = Field(default=None,alias="orientations",)
	outputBins: list[Optional[str]] = Field(alias="outputBins",)
	pagesPerSheet: list[Optional[int]] = Field(alias="pagesPerSheet",)
	qualities: Optional[PrintQuality] = Field(default=None,alias="qualities",)
	rightMargins: list[Optional[int]] = Field(alias="rightMargins",)
	scalings: Optional[PrintScaling] = Field(default=None,alias="scalings",)
	supportsFitPdfToPage: Optional[bool] = Field(default=None,alias="supportsFitPdfToPage",)
	topMargins: list[Optional[int]] = Field(alias="topMargins",)
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

