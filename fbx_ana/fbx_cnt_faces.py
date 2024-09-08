import pyassimp

def print_mesh_count(scene):
    total_vertices = 0
    total_faces = 0

    for index, mesh in enumerate(scene.meshes):
        total_vertices += len(mesh.vertices)
        total_faces += len(mesh.faces)

    print(f"Total Vertices: {total_vertices}")
    print(f"Total Faces: {total_faces}")

def main():
    # 替换为你的 FBX 文件路径
    fbx_filename = "radar_wall.fbx"

    # 使用上下文管理器加载FBX文件
    with pyassimp.load(fbx_filename) as scene:
        if not scene.meshes:
            print(f"No meshes found in {fbx_filename}")
            return

        # 打印网格信息和材质信息
        print_mesh_count(scene)
    
    print(type(scene))

if __name__ == "__main__":
    main()
