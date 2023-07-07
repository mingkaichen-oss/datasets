# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for robomimic_mg dataset."""

from tensorflow_datasets.datasets.robomimic_mg import robomimic_mg_dataset_builder
import tensorflow_datasets.public_api as tfds


class RobomimicMgTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for robomimic_mg dataset."""

  DATASET_CLASS = robomimic_mg_dataset_builder.Builder
  SPLITS = {'train': 2}
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'can_low_dim.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'mg/can_low_dim.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['can_mg_low_dim']


if __name__ == '__main__':
  tfds.testing.test_main()
