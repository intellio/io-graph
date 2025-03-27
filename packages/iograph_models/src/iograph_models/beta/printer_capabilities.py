from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterCapabilities(BaseModel):
	bottomMargins: Optional[list[int]] = Field(alias="bottomMargins", default=None,)
	collation: Optional[bool] = Field(alias="collation", default=None,)
	colorModes: Optional[list[PrintColorMode | str]] = Field(alias="colorModes", default=None,)
	contentTypes: Optional[list[str]] = Field(alias="contentTypes", default=None,)
	copiesPerJob: Optional[IntegerRange] = Field(alias="copiesPerJob", default=None,)
	dpis: Optional[list[int]] = Field(alias="dpis", default=None,)
	duplexModes: Optional[list[PrintDuplexMode | str]] = Field(alias="duplexModes", default=None,)
	feedDirections: Optional[list[PrinterFeedDirection | str]] = Field(alias="feedDirections", default=None,)
	feedOrientations: Optional[list[PrinterFeedOrientation | str]] = Field(alias="feedOrientations", default=None,)
	finishings: Optional[list[PrintFinishing | str]] = Field(alias="finishings", default=None,)
	inputBins: Optional[list[str]] = Field(alias="inputBins", default=None,)
	isColorPrintingSupported: Optional[bool] = Field(alias="isColorPrintingSupported", default=None,)
	isPageRangeSupported: Optional[bool] = Field(alias="isPageRangeSupported", default=None,)
	leftMargins: Optional[list[int]] = Field(alias="leftMargins", default=None,)
	mediaColors: Optional[list[str]] = Field(alias="mediaColors", default=None,)
	mediaSizes: Optional[list[str]] = Field(alias="mediaSizes", default=None,)
	mediaTypes: Optional[list[str]] = Field(alias="mediaTypes", default=None,)
	multipageLayouts: Optional[list[PrintMultipageLayout | str]] = Field(alias="multipageLayouts", default=None,)
	orientations: Optional[list[PrintOrientation | str]] = Field(alias="orientations", default=None,)
	outputBins: Optional[list[str]] = Field(alias="outputBins", default=None,)
	pagesPerSheet: Optional[list[int]] = Field(alias="pagesPerSheet", default=None,)
	qualities: Optional[list[PrintQuality | str]] = Field(alias="qualities", default=None,)
	rightMargins: Optional[list[int]] = Field(alias="rightMargins", default=None,)
	scalings: Optional[list[PrintScaling | str]] = Field(alias="scalings", default=None,)
	supportedColorConfigurations: Optional[list[PrintColorConfiguration | str]] = Field(alias="supportedColorConfigurations", default=None,)
	supportedCopiesPerJob: Optional[IntegerRange] = Field(alias="supportedCopiesPerJob", default=None,)
	supportedDocumentMimeTypes: Optional[list[str]] = Field(alias="supportedDocumentMimeTypes", default=None,)
	supportedDuplexConfigurations: Optional[list[PrintDuplexConfiguration | str]] = Field(alias="supportedDuplexConfigurations", default=None,)
	supportedFinishings: Optional[list[PrintFinishing | str]] = Field(alias="supportedFinishings", default=None,)
	supportedMediaColors: Optional[list[str]] = Field(alias="supportedMediaColors", default=None,)
	supportedMediaSizes: Optional[list[str]] = Field(alias="supportedMediaSizes", default=None,)
	supportedMediaTypes: Optional[list[PrintMediaType | str]] = Field(alias="supportedMediaTypes", default=None,)
	supportedOrientations: Optional[list[PrintOrientation | str]] = Field(alias="supportedOrientations", default=None,)
	supportedOutputBins: Optional[list[str]] = Field(alias="supportedOutputBins", default=None,)
	supportedPagesPerSheet: Optional[IntegerRange] = Field(alias="supportedPagesPerSheet", default=None,)
	supportedPresentationDirections: Optional[list[PrintPresentationDirection | str]] = Field(alias="supportedPresentationDirections", default=None,)
	supportedPrintQualities: Optional[list[PrintQuality | str]] = Field(alias="supportedPrintQualities", default=None,)
	supportsFitPdfToPage: Optional[bool] = Field(alias="supportsFitPdfToPage", default=None,)
	topMargins: Optional[list[int]] = Field(alias="topMargins", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .print_color_mode import PrintColorMode
from .integer_range import IntegerRange
from .print_duplex_mode import PrintDuplexMode
from .printer_feed_direction import PrinterFeedDirection
from .printer_feed_orientation import PrinterFeedOrientation
from .print_finishing import PrintFinishing
from .print_multipage_layout import PrintMultipageLayout
from .print_orientation import PrintOrientation
from .print_quality import PrintQuality
from .print_scaling import PrintScaling
from .print_color_configuration import PrintColorConfiguration
from .integer_range import IntegerRange
from .print_duplex_configuration import PrintDuplexConfiguration
from .print_finishing import PrintFinishing
from .print_media_type import PrintMediaType
from .print_orientation import PrintOrientation
from .integer_range import IntegerRange
from .print_presentation_direction import PrintPresentationDirection
from .print_quality import PrintQuality

