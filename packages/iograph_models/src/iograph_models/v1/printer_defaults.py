from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrinterDefaults(BaseModel):
	colorMode: Optional[PrintColorMode | str] = Field(alias="colorMode", default=None,)
	contentType: Optional[str] = Field(alias="contentType", default=None,)
	copiesPerJob: Optional[int] = Field(alias="copiesPerJob", default=None,)
	dpi: Optional[int] = Field(alias="dpi", default=None,)
	duplexMode: Optional[PrintDuplexMode | str] = Field(alias="duplexMode", default=None,)
	finishings: Optional[list[PrintFinishing | str]] = Field(alias="finishings", default=None,)
	fitPdfToPage: Optional[bool] = Field(alias="fitPdfToPage", default=None,)
	inputBin: Optional[str] = Field(alias="inputBin", default=None,)
	mediaColor: Optional[str] = Field(alias="mediaColor", default=None,)
	mediaSize: Optional[str] = Field(alias="mediaSize", default=None,)
	mediaType: Optional[str] = Field(alias="mediaType", default=None,)
	multipageLayout: Optional[PrintMultipageLayout | str] = Field(alias="multipageLayout", default=None,)
	orientation: Optional[PrintOrientation | str] = Field(alias="orientation", default=None,)
	outputBin: Optional[str] = Field(alias="outputBin", default=None,)
	pagesPerSheet: Optional[int] = Field(alias="pagesPerSheet", default=None,)
	quality: Optional[PrintQuality | str] = Field(alias="quality", default=None,)
	scaling: Optional[PrintScaling | str] = Field(alias="scaling", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .print_color_mode import PrintColorMode
from .print_duplex_mode import PrintDuplexMode
from .print_finishing import PrintFinishing
from .print_multipage_layout import PrintMultipageLayout
from .print_orientation import PrintOrientation
from .print_quality import PrintQuality
from .print_scaling import PrintScaling
