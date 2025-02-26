from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrinterDefaults(BaseModel):
	colorMode: Optional[PrintColorMode] = Field(default=None,alias="colorMode",)
	contentType: Optional[str] = Field(default=None,alias="contentType",)
	copiesPerJob: Optional[int] = Field(default=None,alias="copiesPerJob",)
	dpi: Optional[int] = Field(default=None,alias="dpi",)
	duplexMode: Optional[PrintDuplexMode] = Field(default=None,alias="duplexMode",)
	finishings: Optional[PrintFinishing] = Field(default=None,alias="finishings",)
	fitPdfToPage: Optional[bool] = Field(default=None,alias="fitPdfToPage",)
	inputBin: Optional[str] = Field(default=None,alias="inputBin",)
	mediaColor: Optional[str] = Field(default=None,alias="mediaColor",)
	mediaSize: Optional[str] = Field(default=None,alias="mediaSize",)
	mediaType: Optional[str] = Field(default=None,alias="mediaType",)
	multipageLayout: Optional[PrintMultipageLayout] = Field(default=None,alias="multipageLayout",)
	orientation: Optional[PrintOrientation] = Field(default=None,alias="orientation",)
	outputBin: Optional[str] = Field(default=None,alias="outputBin",)
	pagesPerSheet: Optional[int] = Field(default=None,alias="pagesPerSheet",)
	quality: Optional[PrintQuality] = Field(default=None,alias="quality",)
	scaling: Optional[PrintScaling] = Field(default=None,alias="scaling",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .print_color_mode import PrintColorMode
from .print_duplex_mode import PrintDuplexMode
from .print_finishing import PrintFinishing
from .print_multipage_layout import PrintMultipageLayout
from .print_orientation import PrintOrientation
from .print_quality import PrintQuality
from .print_scaling import PrintScaling

