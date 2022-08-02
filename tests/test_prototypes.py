import os
import logging

import yaml


LOG = logging.getLogger(__name__)


def _check_library(l):
    LOG.debug('checking library %s', l)

    with open(l, 'r') as f:
        library = yaml.safe_load(f)

    assert 'description' in library, f"No description field in {l}"
    assert 'url' in library, f"No url field in {l}"
    assert 'prototypes' in library, f"No prototypes field in {l}"

    for p, prototype in library['prototypes'].iteritems():
        LOG.debug('checking prototype %s', p)
        assert (
            'development_status' in prototype
        ), f"No developement_status field in {l}::{p}"

        assert 'author' in prototype, f"No author field in {l}::{p}"
        assert 'description' in prototype, f"No description field in {l}::{p}"
        assert 'class' in prototype, f"No class field in {l}::{p}"
        assert 'config' in prototype, f"No config field in {l}::{p}"
        assert 'node_type' in prototype, f"No node_type field in {l}::{p}"
        assert 'tags' in prototype, f"No tags field in {l}::{p}"
        assert isinstance(
            prototype['tags'], list
        ), f"Wrong type for attribute tags in {l}::{p}"

        assert 'indicator_types' in prototype, f"No indicator_types field in {l}::{p}"
        assert isinstance(
            prototype['indicator_types'], list
        ), f"Wrong type for attribute indicator_types in {l}::{p}"

        assert len(prototype['indicator_types']), f"0 indicator_types in {l}::{p}"

def test_prototypes():
    libraries = [os.path.join('prototypes', x) for x in os.listdir('prototypes')]

    for l in libraries:
        yield _check_library, l
