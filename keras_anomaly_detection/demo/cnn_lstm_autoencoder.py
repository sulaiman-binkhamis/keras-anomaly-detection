import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from keras_anomaly_detection.library.recurrent import CnnLstmAutoEncoder


def main():
    data_dir_path = '../training/data'
    model_dir_path = '../training/models'
    ecg_data = pd.read_csv(data_dir_path + '/ecg_discord_test.csv', header=None)
    print(ecg_data.head())
    ecg_np_data = ecg_data.as_matrix()
    scaler = MinMaxScaler()
    ecg_np_data = scaler.fit_transform(ecg_np_data)
    print(ecg_np_data.shape)

    ae = CnnLstmAutoEncoder()

    # fit the data and save model into model_dir_path
    ae.fit(ecg_np_data[:23, :], model_dir_path=model_dir_path, estimated_negative_sample_ratio=0.9)

    # load back the model saved in model_dir_path detect anomaly
    ae.load_model(model_dir_path)
    anomaly_information = ae.anomaly(ecg_np_data[:23, :])
    for idx, (is_anomaly, dist) in enumerate(anomaly_information):
        print('# ' + str(idx) + ' is ' + ('abnormal' if is_anomaly else 'normal') + ' (dist: ' + str(dist) + ')')


if __name__ == '__main__':
    main()
