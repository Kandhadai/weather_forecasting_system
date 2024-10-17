# tests/test_educational_content_control.py
import pytest
from HU.Project.Website.controls.educational_content_control import ViewEducationalContentControl


def test_get_content_by_topic(mocker):
    mocker.patch('HU.Project.Website.entities.educational_content.EducationalContent.get_educational_content', return_value=[{'content_type': 'text', 'content': 'Climate change basics'}])

    control = ViewEducationalContentControl()
    content = control.get_content_by_topic('Climate')
    assert len(content) > 0
    assert content[0]['content_type'] == 'text'
