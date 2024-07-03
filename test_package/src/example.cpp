
#include "vivid/vivid.h"

int main() {
    const auto srgb = vivid::srgb_t(vivid::rgb::fromRgb8(vivid::col8_t(255, 0, 255)));
    vivid::rgb::gamma(vivid::lrgb::fromSrgb(srgb), 1.f / 2.0);
}
