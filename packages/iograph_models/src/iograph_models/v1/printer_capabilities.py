from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterCapabilities(BaseModel):
	bottomMargins: Optional[list[int]] = Field(alias="bottomMargins",default=None,)
	collation: Optional[bool] = Field(alias="collation",default=None,)
	colorModes: Optional[PrintColorMode | str] = Field(alias="colorModes",default=None,)
	contentTypes: Optional[list[str]] = Field(alias="contentTypes",default=None,)
	copiesPerJob: Optional[IntegerRange] = Field(alias="copiesPerJob",default=None,)
	dpis: Optional[list[int]] = Field(alias="dpis",default=None,)
	duplexModes: Optional[PrintDuplexMode | str] = Field(alias="duplexModes",default=None,)
	feedOrientations: Optional[PrinterFeedOrientation | str] = Field(alias="feedOrientations",default=None,)
	finishings: Optional[PrintFinishing | str] = Field(alias="finishings",default=None,)
	inputBins: Optional[list[str]] = Field(alias="inputBins",default=None,)
	isColorPrintingSupported: Optional[bool] = Field(alias="isColorPrintingSupported",default=None,)
	isPageRangeSupported: Optional[bool] = Field(alias="isPageRangeSupported",default=None,)
	leftMargins: Optional[list[int]] = Field(alias="leftMargins",default=None,)
	mediaColors: Optional[list[str]] = Field(alias="mediaColors",default=None,)
	mediaSizes: Optional[list[str]] = Field(alias="mediaSizes",default=None,)
	mediaTypes: Optional[list[str]] = Field(alias="mediaTypes",default=None,)
	multipageLayouts: Optional[PrintMultipageLayout | str] = Field(alias="multipageLayouts",default=None,)
	orientations: Optional[PrintOrientation | str] = Field(alias="orientations",default=None,)
	outputBins: Optional[list[str]] = Field(alias="outputBins",default=None,)
	pagesPerSheet: Optional[list[int]] = Field(alias="pagesPerSheet",default=None,)
	qualities: Optional[PrintQuality | str] = Field(alias="qualities",default=None,)
	rightMargins: Optional[list[int]] = Field(alias="rightMargins",default=None,)
	scalings: Optional[PrintScaling | str] = Field(alias="scalings",default=None,)
	supportsFitPdfToPage: Optional[bool] = Field(alias="supportsFitPdfToPage",default=None,)
	topMargins: Optional[list[int]] = Field(alias="topMargins",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .print_color_mode import PrintColorMode
from .integer_range import IntegerRange
from .print_duplex_mode import PrintDuplexMode
from .printer_feed_orientation import PrinterFeedOrientation
from .print_finishing import PrintFinishing
from .print_multipage_layout import PrintMultipageLayout
from .print_orientation import PrintOrientation
from .print_quality import PrintQuality
from .print_scaling import PrintScaling

