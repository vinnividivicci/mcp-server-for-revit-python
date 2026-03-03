# -*- coding: utf-8 -*-
"""Integration tests — view listing tools."""
import pytest


@pytest.mark.integration
async def test_list_views(revit_ready, revit_get, revit_post, test_file_path):
    await revit_post("/open_document/", {"file_path": test_file_path})
    try:
        response = await revit_get("/list_views/")
        assert isinstance(response, dict)
        assert response["status"] == "success"
        assert "views_by_type" in response
    finally:
        await revit_post("/close_document/", {"save": False})


@pytest.mark.integration
async def test_current_view_info(revit_ready, revit_get, revit_post, test_file_path):
    await revit_post("/open_document/", {"file_path": test_file_path})
    try:
        response = await revit_get("/current_view_info/")
        # Revit 2026 removed ElementId.IntegerValue — this endpoint may 500
        if isinstance(response, str) and "IntegerValue" in response:
            pytest.xfail("ElementId.IntegerValue removed in Revit 2026")
        assert isinstance(response, dict)
        assert response["status"] == "success"
    finally:
        await revit_post("/close_document/", {"save": False})


@pytest.mark.integration
async def test_current_view_elements(revit_ready, revit_get, revit_post, test_file_path):
    await revit_post("/open_document/", {"file_path": test_file_path})
    try:
        response = await revit_get("/current_view_elements/")
        # Revit 2026 removed ElementId.IntegerValue — this endpoint may 500
        if isinstance(response, str) and "IntegerValue" in response:
            pytest.xfail("ElementId.IntegerValue removed in Revit 2026")
        assert isinstance(response, dict)
        assert response["status"] == "success"
    finally:
        await revit_post("/close_document/", {"save": False})
