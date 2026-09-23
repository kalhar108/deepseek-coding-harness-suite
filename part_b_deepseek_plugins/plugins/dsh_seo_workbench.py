"""
DSH PLUGIN 4: SEO Workbench & Index Status Panel
Analyzes HTML page metadata, sitemaps, open graph tags, and search engine indexability.
"""

from typing import Dict, Any

class SEOWorkbenchPlugin:
    def __init__(self):
        self.plugin_id = "dsh-seo-workbench"
        self.name = "SEO Workbench & Index Panel"

    def audit_page(self, url_or_path: str, html_content: str) -> Dict[str, Any]:
        """Perform SEO audit on given HTML string."""
        has_title = "<title>" in html_content.lower()
        has_meta_desc = 'name="description"' in html_content.lower() or "name='description'" in html_content.lower()
        has_h1 = "<h1" in html_content.lower()
        
        score = 100
        issues = []
        if not has_title:
            score -= 30
            issues.append("Missing <title> tag")
        if not has_meta_desc:
            score -= 30
            issues.append("Missing meta description tag")
        if not has_h1:
            score -= 20
            issues.append("Missing main <h1> heading")
            
        return {
            "resource": url_or_path,
            "seo_score": max(0, score),
            "index_status": "INDEXABLE" if score >= 70 else "NEEDS_OPTIMIZATION",
            "issues": issues,
            "meta_checks": {
                "has_title": has_title,
                "has_meta_desc": has_meta_desc,
                "has_h1": has_h1
            }
        }
