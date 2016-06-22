/*
 Copyright 2014 Google Inc. All rights reserved.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */

#ifndef DASHTOHLS_DASHTOHLS_API_AVFRAMEWORK_H_
#define DASHTOHLS_DASHTOHLS_API_AVFRAMEWORK_H_

#include <vector>

struct DashToHlsSession;

namespace dash2hls {
  // Encrypt one segment with the global key or return false if encryption
  // failed.
  bool Encrypt(const DashToHlsSession* session, std::vector<uint8_t>* segment);
}  // namespace dash2hls

#endif  // DASHTOHLS_DASHTOHLS_API_AVFRAMEWORK_H_

