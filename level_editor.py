import bpy

# ブレンダーに登録するアドオン情報
bl_info = {
    "name": "レベルエディタ",
    "author": "Rao Kimura",
    "version": (1,0),
    "blender": (3,3,1),
    "location": "",
    "description": "レベルエディタ",
    "warning":"",
    "wiki_url": "",
    "tracker_url": "",
    "category": "object"
}

# メニュー項目描画
def draw_menu_manual(self, context):
    #self : 呼び出し元のクラスインスタンス。C++でいうthisポインタ
    #context : カーソルを合わせた時のポップアップのカスタマイズなど使用

    #トップバーの「エディターメニュー」に項目（オペレータ）を追加
    self.layout.operator("wm.url_open_preset", text="Manual", icon='HELP')

#アドオン有効化時コールバック
def register():
    #メニューに項目を追加
    bpy.types.TOPBAR_MT_editor_menus.append(draw_menu_manual)
    print("レベルエディタが有効化されました。")

#アドオン無効化時コールバック
def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(draw_menu_manual)
    print("レベルエディタが無効化されました。")    

# テスト実行用コード
if __name__ == "__main__":
    register()