# tests/test_educational_content_control.py
import pytest
from HU.Project.Website.controls.educational_content_control import ViewEducationalContentControl
from HU.Project.Website.entities.educational_content import EducationalContent


def test_get_content_by_topic(mocker):
    mocker.patch('HU.Project.Website.entities.educational_content.EducationalContent.get_educational_content',
                 return_value=[
                     EducationalContent(1, "Article", "Weather Basics", "Content about basic weather patterns."),
                     EducationalContent(2, "Video", "Weather Basics", "Video explaining weather basics."),
                 ])

    control = ViewEducationalContentControl()
    content = control.get_content_by_topic("Weather Basics")

    assert len(content) == 2
    assert content[0].content_type == "Article"
    assert content[1].content_type == "Video"


def test_get_all_content(mocker):
    mocker.patch('HU.Project.Website.entities.educational_content.EducationalContent.get_all_content', return_value=[
        EducationalContent(1, "Article", "Weather Basics", "Content about basic weather patterns."),
        EducationalContent(2, "Article", "Storm Preparation", "How to prepare for storms."),
    ])

    control = ViewEducationalContentControl()
    content = control.get_all_content()

    assert len(content) == 2
    assert content[0].topic == "Weather Basics"
    assert content[1].topic == "Storm Preparation"

