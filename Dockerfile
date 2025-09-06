FROM rockylinux:9.3


RUN set -eux; \
    dnf install -y epel-release && \
    dnf install -y --allowerasing \
        curl \
        libX11 libXext libXt libXi libXtst libXmu libXpm \
        libXft libXcursor libXinerama libXcomposite libXdamage libXrender libXrandr \
        mesa-libGL mesa-libGLU libglvnd-opengl \
        libSM libICE freetype fontconfig \
        liberation-fonts dejavu-sans-fonts urw-base35-fonts \
        libxkbcommon libtiff \
        libglvnd-egl libva libvdpau nss nspr alsa-lib libxkbfile && \
    dnf clean all && rm -rf /var/cache/dnf

ENV PYTHONDONTWRITEBYTECODE=1 \
    MAYA_LOCATION=/usr/autodesk/maya2026/ \
    PATH=/usr/autodesk/maya2026/bin:$PATH

RUN set -eux; \
    curl -L -o /maya.tgz "https://efulfillment.autodesk.com/NetSWDLD/prd/2026/MAYA/901073B8-F0A1-3952-A459-9CA36A875C41/Autodesk_Maya_2026_2_Update_Linux_64bit.tgz" && \
    mkdir /maya_install && \
    tar -xvf /maya.tgz -C /maya_install && \
    rpm --force -ivh /maya_install/Packages/Maya2026_64-*.x86_64.rpm && \
    rm -rf /maya.tgz /maya_install && \
    rm -rf /usr/autodesk/maya2026/{Examples,brushImages,icons,include,presets,qml,synColor,translations}
