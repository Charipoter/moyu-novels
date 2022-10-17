from backend.service.NovelReadService import novel_read_service
from backend.service.NovelDisplayService import novel_display_service
from backend.controller.ReadPageController import read_page_controller
from backend.controller.DisplayPageController import display_page_controller
from backend.controller.InitController import init_controller


class DataBaseTest:

    def delete_all(self):
        novel_read_service.delete_chapter_basic_infos_from_db()
        novel_display_service.delete_novel_display_infos_from_db()
        novel_display_service.delete_novel_covers_from_resource()

    # 5部小说花费18秒
    def create_by_novel_basic_infos(self):
        l = display_page_controller.get_novel_basic_infos()
        display_page_controller.get_novel_display_infos()

        for o in l.values():
            read_page_controller.get_chapter_basic_infos_by_basic_object(o)

    def delete_all_and_create_by_novel_basic_infos(self):
        novel_read_service.delete_chapter_basic_infos_from_db()
        novel_display_service.delete_novel_display_infos_from_db()
        novel_display_service.delete_novel_covers_from_resource()

        l = display_page_controller.get_novel_basic_infos()
        display_page_controller.get_novel_display_infos()

        for o in l.values():
            read_page_controller.get_novel_all_chapters_basic_info_by_object(o)
            read_page_controller.get_chapter_basic_infos_by_basic_object(o)

    # 5部小说花费9秒
    def test_init(self):
        init_controller.init_all_novels_needy_data()


if __name__ == "__main__":
    t = DataBaseTest()
    t.delete_all()
