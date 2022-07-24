from pyodide import create_proxy
from js import THREE, window, document

class App:
    def __init__(self) -> None:
        self._resources = {}

    def add_resource(self,name,value)->None:
        self._resources[name] = value

    def run(self) -> None:
        self._setup_resources()

    def _setup_resources(self)->None:
        if "container" in self._resources:
            self._container = document.querySelector(self._resources['container'])



scene = THREE.Scene.new();
scene.background = THREE.Color.new('black');

fov = 35
aspect = container.clientWidth/container.clientHeight
near = 0.1
far = 100

camera = THREE.PerspectiveCamera.new(fov, aspect, near, far)

camera.position.set(0,0,10)

renderer = THREE.WebGLRenderer.new()
renderer.setSize(container.clientWidth, container.clientHeight)
renderer.setPixelRatio(window.devicePixelRatio)

geometry = THREE.BoxGeometry.new()
material = THREE.MeshBasicMaterial.new(color="#00ff00")
cube = THREE.Mesh.new( geometry, material )
scene.add( cube )

renderer.render( scene, camera )

def animate(*args):
    window.requestAnimationFrame( create_proxy(animate) )
    cube.rotation.x += 0.01
    cube.rotation.y += 0.01
    renderer.render( scene, camera )

animate()

container.append(renderer.domElement);