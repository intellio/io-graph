from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RegionalAndLanguageSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	authoringLanguages: Optional[list[LocaleInfo]] = Field(alias="authoringLanguages", default=None,)
	defaultDisplayLanguage: Optional[LocaleInfo] = Field(alias="defaultDisplayLanguage", default=None,)
	defaultRegionalFormat: Optional[LocaleInfo] = Field(alias="defaultRegionalFormat", default=None,)
	defaultSpeechInputLanguage: Optional[LocaleInfo] = Field(alias="defaultSpeechInputLanguage", default=None,)
	defaultTranslationLanguage: Optional[LocaleInfo] = Field(alias="defaultTranslationLanguage", default=None,)
	regionalFormatOverrides: Optional[RegionalFormatOverrides] = Field(alias="regionalFormatOverrides", default=None,)
	translationPreferences: Optional[TranslationPreferences] = Field(alias="translationPreferences", default=None,)

from .locale_info import LocaleInfo
from .locale_info import LocaleInfo
from .locale_info import LocaleInfo
from .locale_info import LocaleInfo
from .locale_info import LocaleInfo
from .regional_format_overrides import RegionalFormatOverrides
from .translation_preferences import TranslationPreferences

