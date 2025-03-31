from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TranslationPreferences(BaseModel):
	languageOverrides: Optional[list[TranslationLanguageOverride]] = Field(alias="languageOverrides", default=None,)
	translationBehavior: Optional[TranslationBehavior | str] = Field(alias="translationBehavior", default=None,)
	untranslatedLanguages: Optional[list[str]] = Field(alias="untranslatedLanguages", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .translation_language_override import TranslationLanguageOverride
from .translation_behavior import TranslationBehavior
