{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05") {} }:

pkgs.mkShellNoCC {
  packages = with pkgs; [
    python312
    python312Packages.paho-mqtt
    python312Packages.yamllint
    python312Packages.requests
    python312Packages.pytz
    python312Packages.jinja2
    mosquitto
  ];
}
