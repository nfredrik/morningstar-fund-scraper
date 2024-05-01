import re
from urllib.request import Request, urlopen


class FundException(Exception):
    ...


class Fund:
    BASE_URL = "https://www.morningstar.se/se/funds/snapshot/snapshot.aspx?id="

    def __init__(self, perfid: str = "0P0000IWH7"):
        if not isinstance(perfid, str):
            raise FundException(f"Invalid perfId: {perfid}")

        self.perfid = perfid

    def get_nav(self) -> dict:
        url = f"{self.BASE_URL}{self.perfid}"
        response = self._fetch_page(url)
        fund_name = self._extract_fund_name(response)
        nav_data = self._extract_nav_data(response)
        return {
            "fund": fund_name,
            "nav": nav_data[2],
            "currency": nav_data[1],
            "the_date": nav_data[0],
        }

    def _fetch_page(self, url: str) -> str:
        req = Request(url, headers={"User-Agent": "tutan"})
        with urlopen(req) as response:
            tmp = response.read().decode("utf-8")
            return re.sub(r"\s+", " ", tmp)

    def _extract_fund_name(self, html: str) -> str:
        match = re.search(r"<h1>(.*?)</h1>", html)
        if match:
            return match.group(1)

        raise FundException("Error, failed to extract fund name")

    def _extract_nav_data(self, html: str) -> tuple:
        match = re.search(
            r"<br \/>([\d\-]+)<\/span><\/td><td class=\"line\"> <\/td><td class=\"line text\">(\w+)([,\d\ ]+)<\/td>",
            html,
        )
        if match:
            return (
                match.group(1).replace(",", ".").replace(" ", ""),
                match.group(2),
                match.group(3).replace(" ", ""),
            )

        raise FundException("Error, failed to extract NAV data")
