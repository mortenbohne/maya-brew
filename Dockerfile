FROM rockylinux:9.3

ENV PYTHONDONTWRITEBYTECODE=1 \
    MAYA_LOCATION=/usr/autodesk/maya2026 \
    PATH=/usr/autodesk/maya2026/bin:$PATH

RUN set -eux; \
    dnf install -y epel-release && \
    dnf install -y --allowerasing \
        curl \
        libX11 libXext libXt libXi libXtst libXmu libXpm \
        libXft libXcursor libXinerama libXcomposite libXdamage libXrender libXrandr \
        mesa-libGL mesa-libGLU libglvnd-opengl libglvnd-egl \
        libSM libICE freetype fontconfig \
        libxkbcommon libxkbfile \
        libtiff \
        libva libvdpau \
        nss nspr \
        alsa-lib && \
    dnf clean all && rm -rf /var/cache/dnf

# Download & install Maya
RUN set -eux; \
    curl -L -o /maya.tgz "https://efulfillment.autodesk.com/NetSWDLD/prd/2026/MAYA/901073B8-F0A1-3952-A459-9CA36A875C41/Autodesk_Maya_2026_2_Update_Linux_64bit.tgz" && \
    mkdir /maya_install && \
    tar -xf /maya.tgz -C /maya_install && \
    rpm --force -ivh /maya_install/Packages/Maya2026_64-*.x86_64.rpm && \
    rm -rf /maya.tgz /maya_install && \
    rm -rf /usr/autodesk/maya2026/{Examples,brushImages,icons,include,presets,qml,synColor,translations}

# Add healthcheck script and non-root user
RUN set -eux; \
    printf '#!/usr/bin/env bash\nset -e\n[ -x "$MAYA_LOCATION/bin/maya" ] || exit 1\nexit 0\n' >/usr/local/bin/healthcheck && \
    chmod +x /usr/local/bin/healthcheck && \
    groupadd -r maya && useradd -r -g maya -d /home/maya -m maya

HEALTHCHECK --interval=30m --timeout=30s --start-period=30s --retries=3 CMD ["/usr/local/bin/healthcheck"]

WORKDIR /home/maya
USER maya
