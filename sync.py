from magento_quotes import email_unpaid_quotes
import logging
import logging.config
import os


def main():
    config_file = os.path.join(os.path.dirname(__file__),
                               'logging.conf')

    logging.config.fileConfig(config_file)
    logging.info('starting')

    email_unpaid_quotes()

    logging.info('finished')


if __name__ == "__main__":
    main()
