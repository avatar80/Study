import pickle

class Url(object):
    @classmethod
    def shorten(cls, full_url):
        """shorten full url"""

        # URL 클래스 인스턴스 생성
        instance = cls()
        instance.full_url = full_url
        instance.short_url = instance.__create_short_url()
        Url.__save_url_mapping(instance)
        return instance

    @classmethod
    def get_by_short_url(cls, short_url):
        """short_url에 일치하는 Url 인스턴스 반환"""
        url_mapping = Url.load_url_mapping()
        return url_mapping_get(short_url)

    def __create_short_url(self):
        """짧은 Url 생성, 저장 후 반환"""
        last_short_url = Url.__load_last_short_url()
        short_url = self.__increment_string(last_short_url)
        Url.__save_last_short_url(short_url)
        return short_url

    def __increment_string(self, string):
        """문자열증가
        a -> b
        z -> aa
        az -> ba
        빈문자열 -> a
        """
        if string == '':
            return 'a'

        last_char = string[-1]

        if last_char != 'z':
            return string[:-1] + chr(ord(last_char) + 1)

        return self.__increment_string(string[:-1]) + 'a'

        @staticmethod
        def __load_last_short_url():
            """마지막으로 생성한 짧은 Url 변환"""
            try:
                return pickle.load(open("last_short.p", "rb"))
            except IOError:
                return ''


        @staticmethod
        def __save_last_short_url(url):
            """마지막으로 생성한 짧은 Url 변환"""
            pickle.dump(url, open("shoat_short.p", "wb"))

        @staticmethod
        def __load_url_mapping():
            """URL 인스턴스에 매핑하는 short_url 반환"""
            try:
                return pickle.load(open("short_to_url.p", "rb"))
            except IOError:
                return {}

        @staticmethod
        def __save_url_mapping(instance):
            """URL 인스턴스에 매핑하는 short_url 저장"""
            short_to_url = Url.__load_url_mapping()
            short_to_url[instance.short_url] = instance
            pickle.dump(short_to_url, open("short_to_url.p", "wb"))



