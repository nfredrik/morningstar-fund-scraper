import os
from datetime import datetime

import pytest
from unittest.mock import patch

from assertpy import assert_that, soft_assertions
from dateutil.parser import parse
from morningstar_fund_scraper import Fund, FundException

IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"


@pytest.fixture
def mock_response():
    return """
    <tr><td><div class="snapshotTitleBox"><h1>SEB Rysslandfond C EUR - Lux</h1><span class="div_title_MQR"><span
    <h2>SEB Rysslandfond C EUR - Lux</h2>uicktake1_col333_OverviewGeneralItem1_ctl04\" class=\"FlowLayout
        Default  layout content\">\r\n\t\t\t\t\t\t<table class=\"alternated
        toplist
        halftoplist\" border=\"0\">\r\n\t\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t\t
        <td>Senaste NAV</td><td>  738,16 SEK</td><td>2018-11-16</td>\r\n\t\t\t\t\t\t\t</tr><tr
        tr><td class="line heading">Andelskurs (NAV)<span class="heading"><br />2024-04-29</span></td><td class="line"> </td><td class="line text">SEK 452,35</td></tr><tr><td class="line heading">Ändring NAV en dag</td><td
    """


@patch("morningstar_fund_scraper.Fund._fetch_page")
def test_get_nav(mock_fetch_page, mock_response):
    mock_fetch_page.return_value = mock_response

    # Create an instance of the Fund class
    fund = Fund()

    # Call the get_nav method
    result = fund.get_nav()

    assert_that(result).is_equal_to(
        {
            "fund": "SEB Rysslandfond C EUR - Lux",
            "nav": "452,35",
            "currency": "SEK",
            "date": "2024-04-29",
        }
    )


def test_get_nav_bad_input():
    with pytest.raises(FundException):
        Fund(perfid=1234)


@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Do not test this in Github Actions.")
def test_get_nav_real():
    fund = Fund(perfid="F00000PYZ6")
    result = fund.get_nav()
    with soft_assertions():
        assert_that(result["fund"]).is_type_of(str)
        assert_that(result["nav"]).is_type_of(str)
        assert_that(result["currency"]).is_type_of(str)
        assert_that(parse(result["date"])).is_type_of(datetime)
