import pyassimp

def print_mesh_info(scene):
    for index, mesh in enumerate(scene.meshes):
        print(f"Mesh {index + 1} - Name: {mesh.name}")
        
        if mesh.materialindex < len(scene.materials):
            material = scene.materials[mesh.materialindex]
            print("  Material Information:")
            
            # 打印材质的属性
            for key, value in material.properties.items():
                print(f"    {key}: {value}")

        else:
            print("  No material associated with this mesh.")
            
        print("")

def main():
    # 替换为你的 FBX 文件路径
    fbx_filename = "radar_wall.fbx"

    # 使用上下文管理器加载FBX文件
    with pyassimp.load(fbx_filename) as scene:
        if not scene.meshes:
            print(f"No meshes found in {fbx_filename}")
            return

        # 打印材质信息
        print_mesh_info(scene)
    
    print(type(scene))

if __name__ == "__main__":
    main()
