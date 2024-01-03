import streamlit as st 
import pandas
import numpy
import time

# 设置全局属性
st.set_page_config(
    page_title='我是标题',
    page_icon=' ',
    layout='wide'
)

# 正文
with st.sidebar:
    st.title('欢迎来到我的应用')
    st.markdown('---')
    st.markdown('这是它的特性：\n- feature 1\n- feature 2\n- feature 3')

st.title('Python 不同的库实现图像读入成 numpy 数组')
tab1, tab2, tab3 = st.tabs(['opencv', 'pillow', 'imageio'])

with tab1:
    st.write('欢迎来到我的应用嘛')
    url = st.text_input('请输入要爬取的网页 URL')
    st.write(pandas.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    }))
    '''
    ```python
    import cv2
    image = cv2.imread('image.png')
    ```
    '''
    option = st.sidebar.selectbox(
        'Which number do you like best?',
        #pandas.DataFrame({'first column': [1, 2, 3, 4]}))
        [1,2,3])

    'You selected: ', option

with tab2:
    '''
    python
    from PIL import Image
    image = Image.open('image.png')
    '''
    map_data = pandas.DataFrame(
    numpy.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(map_data)

with tab3:
    '''
    ```python
    import imageio
    image = imageio.imread('image.png')
    ```
    '''
    if st.checkbox('Show dataframe'):
        chart_data = pandas.DataFrame(
        numpy.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        st.line_chart(chart_data)

    latest_iteration = st.empty()

    bar = st.progress(0)

    for i in range(100):
    # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

'...and now we\'re done!'



## 默认渲染到主界面
st.title('这是主界面')
st.info('这是主界面内容')

