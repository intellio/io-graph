from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingGermany(BaseModel):
	movieRating: Optional[RatingGermanyMoviesType | str] = Field(alias="movieRating", default=None,)
	tvRating: Optional[RatingGermanyTelevisionType | str] = Field(alias="tvRating", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .rating_germany_movies_type import RatingGermanyMoviesType
from .rating_germany_television_type import RatingGermanyTelevisionType

