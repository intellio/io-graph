from __future__ import annotations
from enum import StrEnum


class PrintFinishing(StrEnum):
	none = "none"
	staple = "staple"
	punch = "punch"
	cover = "cover"
	bind = "bind"
	saddleStitch = "saddleStitch"
	stitchEdge = "stitchEdge"
	stapleTopLeft = "stapleTopLeft"
	stapleBottomLeft = "stapleBottomLeft"
	stapleTopRight = "stapleTopRight"
	stapleBottomRight = "stapleBottomRight"
	stitchLeftEdge = "stitchLeftEdge"
	stitchTopEdge = "stitchTopEdge"
	stitchRightEdge = "stitchRightEdge"
	stitchBottomEdge = "stitchBottomEdge"
	stapleDualLeft = "stapleDualLeft"
	stapleDualTop = "stapleDualTop"
	stapleDualRight = "stapleDualRight"
	stapleDualBottom = "stapleDualBottom"
	unknownFutureValue = "unknownFutureValue"
	stapleTripleLeft = "stapleTripleLeft"
	stapleTripleTop = "stapleTripleTop"
	stapleTripleRight = "stapleTripleRight"
	stapleTripleBottom = "stapleTripleBottom"
	bindLeft = "bindLeft"
	bindTop = "bindTop"
	bindRight = "bindRight"
	bindBottom = "bindBottom"
	foldAccordion = "foldAccordion"
	foldDoubleGate = "foldDoubleGate"
	foldGate = "foldGate"
	foldHalf = "foldHalf"
	foldHalfZ = "foldHalfZ"
	foldLeftGate = "foldLeftGate"
	foldLetter = "foldLetter"
	foldParallel = "foldParallel"
	foldPoster = "foldPoster"
	foldRightGate = "foldRightGate"
	foldZ = "foldZ"
	foldEngineeringZ = "foldEngineeringZ"
	punchTopLeft = "punchTopLeft"
	punchBottomLeft = "punchBottomLeft"
	punchTopRight = "punchTopRight"
	punchBottomRight = "punchBottomRight"
	punchDualLeft = "punchDualLeft"
	punchDualTop = "punchDualTop"
	punchDualRight = "punchDualRight"
	punchDualBottom = "punchDualBottom"
	punchTripleLeft = "punchTripleLeft"
	punchTripleTop = "punchTripleTop"
	punchTripleRight = "punchTripleRight"
	punchTripleBottom = "punchTripleBottom"
	punchQuadLeft = "punchQuadLeft"
	punchQuadTop = "punchQuadTop"
	punchQuadRight = "punchQuadRight"
	punchQuadBottom = "punchQuadBottom"
	fold = "fold"
	trim = "trim"
	bale = "bale"
	bookletMaker = "bookletMaker"
	coat = "coat"
	laminate = "laminate"
	trimAfterPages = "trimAfterPages"
	trimAfterDocuments = "trimAfterDocuments"
	trimAfterCopies = "trimAfterCopies"
	trimAfterJob = "trimAfterJob"

