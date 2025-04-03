from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ReadingAssignmentSubmission(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.readingAssignmentSubmission"] = Field(alias="@odata.type", default="#microsoft.graph.readingAssignmentSubmission")
	accuracyScore: float | str | ReferenceNumeric
	action: Optional[str] = Field(alias="action", default=None,)
	assignmentId: Optional[str] = Field(alias="assignmentId", default=None,)
	challengingWords: Optional[list[ChallengingWord]] = Field(alias="challengingWords", default=None,)
	classId: Optional[str] = Field(alias="classId", default=None,)
	insertions: Optional[int] = Field(alias="insertions", default=None,)
	mispronunciations: Optional[int] = Field(alias="mispronunciations", default=None,)
	missedExclamationMarks: Optional[int] = Field(alias="missedExclamationMarks", default=None,)
	missedPeriods: Optional[int] = Field(alias="missedPeriods", default=None,)
	missedQuestionMarks: Optional[int] = Field(alias="missedQuestionMarks", default=None,)
	missedShorts: Optional[int] = Field(alias="missedShorts", default=None,)
	monotoneScore: float | str | ReferenceNumeric
	omissions: Optional[int] = Field(alias="omissions", default=None,)
	repetitions: Optional[int] = Field(alias="repetitions", default=None,)
	selfCorrections: Optional[int] = Field(alias="selfCorrections", default=None,)
	studentId: Optional[str] = Field(alias="studentId", default=None,)
	submissionDateTime: Optional[datetime] = Field(alias="submissionDateTime", default=None,)
	submissionId: Optional[str] = Field(alias="submissionId", default=None,)
	unexpectedPauses: Optional[int] = Field(alias="unexpectedPauses", default=None,)
	wordCount: Optional[int] = Field(alias="wordCount", default=None,)
	wordsPerMinute: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .challenging_word import ChallengingWord
