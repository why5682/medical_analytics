"""
Journal Configuration
Defines available medical journals and their RSS feeds.
Categorized by MEDICAL SPECIALTY.
"""

JOURNALS = [
    # ========================================
    # Pharmacoepidemiology & Drug Safety
    # ========================================
    {
        "name": "Pharmacoepidemiology and Drug Safety",
        "url": "https://onlinelibrary.wiley.com/feed/10991557/most-recent",
        "category": "Pharmacoepidemiology"
    },
    {
        "name": "Drug Safety",
        "url": "https://link.springer.com/search.rss?facet-content-type=Article&facet-journal-id=40264&channel-name=Drug%20Safety",
        "category": "Pharmacoepidemiology"
    },
    
    # ========================================
    # Clinical Pharmacology
    # ========================================
    {
        "name": "Clinical Pharmacology & Therapeutics",
        "url": "https://onlinelibrary.wiley.com/feed/15326535/most-recent",
        "category": "Clinical Pharmacology"
    },
    {
        "name": "British Journal of Clinical Pharmacology",
        "url": "https://onlinelibrary.wiley.com/feed/13652125/most-recent",
        "category": "Clinical Pharmacology"
    },
    
    # ========================================
    # General Medicine (Top Tier)
    # ========================================
    {
        "name": "NEJM",
        "url": "https://www.nejm.org/action/showFeed?type=etoc&feed=rss&jc=nejm",
        "category": "General Medicine"
    },
    {
        "name": "The Lancet",
        "url": "https://www.thelancet.com/rssfeed/lancet_current.xml",
        "category": "General Medicine"
    },
    {
        "name": "JAMA",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jama&hl=en-US&gl=US&ceid=US:en",
        "category": "General Medicine"
    },
    {
        "name": "JAMA Internal Medicine",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jamainternalmedicine&hl=en-US&gl=US&ceid=US:en",
        "category": "General Medicine"
    },
    {
        "name": "The BMJ",
        "url": "https://www.bmj.com/rss/recent.xml",
        "category": "General Medicine"
    },
    {
        "name": "JAMA Network Open",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jamanetworkopen&hl=en-US&gl=US&ceid=US:en",
        "category": "General Medicine"
    },
    {
        "name": "BMJ Open",
        "url": "https://bmjopen.bmj.com/rss/recent.xml",
        "category": "General Medicine"
    },

    # ========================================
    # Oncology (종양학)
    # ========================================
    {
        "name": "The Lancet Oncology",
        "url": "https://www.thelancet.com/rssfeed/lanonc_current.xml",
        "category": "Oncology"
    },
    {
        "name": "JAMA Oncology",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jamaoncology&hl=en-US&gl=US&ceid=US:en",
        "category": "Oncology"
    },

    # ========================================
    # Cardiology (심장내과)
    # ========================================
    {
        "name": "JAMA Cardiology",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jamacardiology&hl=en-US&gl=US&ceid=US:en",
        "category": "Cardiology"
    },
    {
        "name": "Heart",
        "url": "https://heart.bmj.com/rss/recent.xml",
        "category": "Cardiology"
    },

    # ========================================
    # Neurology (신경과)
    # ========================================
    {
        "name": "The Lancet Neurology",
        "url": "https://www.thelancet.com/rssfeed/laneur_current.xml",
        "category": "Neurology"
    },
    {
        "name": "JAMA Neurology",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jamaneurology&hl=en-US&gl=US&ceid=US:en",
        "category": "Neurology"
    },
    {
        "name": "JNNP",
        "url": "https://jnnp.bmj.com/rss/recent.xml",
        "category": "Neurology"
    },

    # ========================================
    # Psychiatry (정신건강의학과)
    # ========================================
    {
        "name": "The Lancet Psychiatry",
        "url": "https://www.thelancet.com/rssfeed/lanpsy_current.xml",
        "category": "Psychiatry"
    },
    {
        "name": "JAMA Psychiatry",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jamapsychiatry&hl=en-US&gl=US&ceid=US:en",
        "category": "Psychiatry"
    },

    # ========================================
    # Diabetes/Endocrinology (내분비내과)
    # ========================================
    {
        "name": "The Lancet Diabetes & Endocrinology",
        "url": "https://www.thelancet.com/rssfeed/landia_current.xml",
        "category": "Diabetes/Endocrinology"
    },

    # ========================================
    # Gastroenterology (소화기내과)
    # ========================================
    {
        "name": "The Lancet Gastroenterology & Hepatology",
        "url": "https://www.thelancet.com/rssfeed/langas_current.xml",
        "category": "Gastroenterology"
    },
    {
        "name": "Gut",
        "url": "https://gut.bmj.com/rss/recent.xml",
        "category": "Gastroenterology"
    },

    # ========================================
    # Respiratory (호흡기내과)
    # ========================================
    {
        "name": "The Lancet Respiratory Medicine",
        "url": "https://www.thelancet.com/rssfeed/lanres_current.xml",
        "category": "Respiratory"
    },
    {
        "name": "Thorax",
        "url": "https://thorax.bmj.com/rss/recent.xml",
        "category": "Respiratory"
    },

    # ========================================
    # Infectious Disease (감염내과)
    # ========================================
    {
        "name": "The Lancet Infectious Diseases",
        "url": "https://www.thelancet.com/rssfeed/laninf_current.xml",
        "category": "Infectious Disease"
    },

    # ========================================
    # Public Health (공중보건)
    # ========================================
    {
        "name": "The Lancet Global Health",
        "url": "https://www.thelancet.com/rssfeed/langlo_current.xml",
        "category": "Public Health"
    },
    {
        "name": "The Lancet Public Health",
        "url": "https://www.thelancet.com/rssfeed/lanpub_current.xml",
        "category": "Public Health"
    },

    # ========================================
    # Pediatrics (소아청소년과)
    # ========================================
    {
        "name": "JAMA Pediatrics",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jamapediatrics&hl=en-US&gl=US&ceid=US:en",
        "category": "Pediatrics"
    },

    # ========================================
    # Surgery (외과)
    # ========================================
    {
        "name": "JAMA Surgery",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jamasurgery&hl=en-US&gl=US&ceid=US:en",
        "category": "Surgery"
    },

    # ========================================
    # Dermatology (피부과)
    # ========================================
    {
        "name": "JAMA Dermatology",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jamadermatology&hl=en-US&gl=US&ceid=US:en",
        "category": "Dermatology"
    },

    # ========================================
    # Ophthalmology (안과)
    # ========================================
    {
        "name": "JAMA Ophthalmology",
        "url": "https://news.google.com/rss/search?q=site:jamanetwork.com/journals/jamaophthalmology&hl=en-US&gl=US&ceid=US:en",
        "category": "Ophthalmology"
    },

    # ========================================
    # Rheumatology (류마티스내과)
    # ========================================
    {
        "name": "Annals of the Rheumatic Diseases",
        "url": "https://ard.bmj.com/rss/recent.xml",
        "category": "Rheumatology"
    },

    # ========================================
    # Sports Medicine (스포츠의학)
    # ========================================
    {
        "name": "British Journal of Sports Medicine",
        "url": "https://bjsm.bmj.com/rss/recent.xml",
        "category": "Sports Medicine"
    },

    # ========================================
    # Healthcare Quality (의료 질 관리)
    # ========================================
    {
        "name": "BMJ Quality & Safety",
        "url": "https://qualitysafety.bmj.com/rss/recent.xml",
        "category": "Healthcare Quality"
    },
]


def get_journals_by_category():
    """Group journals by category (medical specialty)."""
    categories = {}
    for journal in JOURNALS:
        cat = journal.get("category", "Other")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(journal)
    return categories


def get_journal_names():
    """Get list of all journal names."""
    return [j["name"] for j in JOURNALS]
