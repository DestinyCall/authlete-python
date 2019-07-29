#
# Copyright (C) 2019 Authlete, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the
# License.


from enum import Enum


class JWEEnc(Enum):
    A128CBC_HS256 = 'A128CBC-HS256'
    A192CBC_HS384 = 'A192CBC-HS384'
    A256CBC_HS512 = 'A256CBC-HS512'
    A128GCM       = 'A128GCM'
    A192GCM       = 'A192GCM'
    A256GCM       = 'A256GCM'
