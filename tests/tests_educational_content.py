from HU.Project.Website.entities.educational_content import EducationalContent


def test_get_educational_content_by_topic(mocker):
    mocker.patch('HU.Project.Website.dao.EducationalContent_dao.EducationalContentDAO.get_educational_content',
                 return_value=[
                     (1, "article", "Weather Basics", "Understanding weather patterns."),
                     (2, "video", "Weather Basics", "Introduction to meteorology.")
                 ])

    content = EducationalContent.get_educational_content("Weather Basics")
    assert len(content) == 2
    assert content[0].content_type == "article"
    assert content[1].content_type == "video"


def test_categorize_educational_content():
    content_list = [
        EducationalContent(1, "article", "Weather Basics", "Understanding weather patterns."),
        EducationalContent(2, "video", "Advanced Meteorology", "Detailed analysis of storm systems."),
        EducationalContent(3, "article", "Weather Basics", "Basic concepts of meteorology.")
    ]

    categorized_content = EducationalContent.categorize_content(content_list)

    assert len(categorized_content["Weather Basics"]) == 2
    assert len(categorized_content["Advanced Meteorology"]) == 1


