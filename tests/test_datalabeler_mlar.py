"""
Tests for DataLabeler using different sample type
"""

import copy
from ..data_labeling.labeling import DataLabeler
from pytest import fixture


def test_dataLabeler_mlar(example_dataset_adi):
    """
    Parameters
    ----------
    example_dataset_adi : fixture
        Taken automatically from ``conftest.py``.
    """

    dataset = copy.copy(example_dataset_adi)

    radius_int = round(dataset.fwhm*2)

    print("distances taken at min radius : {}".format(radius_int))

    if dataset.cube.shape[0] > 80:
        dataset.cube = dataset.cube[0:80]
        dataset.angles = dataset.angles[0:80]

    try:
        labeler = DataLabeler('mlar', dataset.cube, dataset.angles,
                              dataset.psf, radius_int=radius_int,
                              fwhm=dataset.fwhm, plsc=0.02719,
                              min_snr=3, max_snr=5, n_proc=2)
    except TypeError:
        raise

    try:
        labeler.estimate_fluxes(plot=False)
    except TypeError:
        raise

    try:
        labeler.run()
    except TypeError:
        raise

    try:
        labeler.augment()
    except TypeError:
        raise

    return True