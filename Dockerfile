FROM rockylinux:9.3

RUN dnf install epel-release -y && \
    dnf install -y --allowerasing \
    curl \
    libX11 \
    libXext \
    libXt \
    libXi \
    libXtst \
    libXmu \
    libXpm \
    libXft \
    libXcursor \
    libXinerama \
    libXcomposite \
    libXdamage \
    libXrender \
    libXrandr \
    mesa-libGL \
    mesa-libGLU \
    libglvnd-opengl \
    libSM \
    libICE \
    freetype \
    fontconfig \
    liberation-fonts \
    dejavu-sans-fonts \
    urw-base35-fonts \
    libxkbcommon \
    libtiff && \
    dnf clean all

ENV PYTHONDONTWRITEBYTECODE=1

# Download Maya installer
RUN curl -L -o /maya.tgz "https://efulfillment.autodesk.com/NetSWDLD/prd/2026/MAYA/901073B8-F0A1-3952-A459-9CA36A875C41/Autodesk_Maya_2026_2_Update_Linux_64bit.tgz"

# Extract Maya installer
RUN mkdir /maya_install && \
    tar -xvf /maya.tgz -C /maya_install && \
    rm -rf /maya.tgz

# Install Maya packages
RUN rpm --force -ivh /maya_install/Packages/Maya2026_64-*.x86_64.rpm

# Clean up installer
RUN rm -rf /maya_install

# Remove unnecessary Maya files
RUN rm -rf /usr/autodesk/maya2026/Examples && \
    rm -rf /usr/autodesk/maya2026/brushImages && \
    rm -rf /usr/autodesk/maya2026/icons && \
    rm -rf /usr/autodesk/maya2026/include && \
    rm -rf /usr/autodesk/maya2026/presets && \
    rm -rf /usr/autodesk/maya2026/qml && \
    rm -rf /usr/autodesk/maya2026/synColor && \
    rm -rf /usr/autodesk/maya2026/translations

ENV MAYA_LOCATION=/usr/autodesk/maya2026/
ENV PATH=$MAYA_LOCATION/bin:$PATH

# Debugging layer - add missing packages here as you find them
RUN dnf install -y --allowerasing libglvnd-egl libva libvdpau nss nspr alsa-lib libxkbfile && dnf clean all
