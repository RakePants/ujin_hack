
import { Avatar, Button, Table, TableProps, Tag } from 'antd';
import { useEffect, useRef, useState } from 'react';
import { $api } from 'shared/api/api';

import { LogSchema } from '../model/types/LogSchema';
import * as cls from './Logs.module.scss'
import { ArrowDownOutlined } from '@ant-design/icons';
interface LogsProps {
    className?: string
}
const dateOptions: Intl.DateTimeFormatOptions = {
    day: "numeric",
    month: "numeric",
    year: "numeric",
    hour: "numeric",
    minute: "numeric",
    second: "numeric"
}
const columns: TableProps<LogSchema>['columns'] = [
    {
        title: 'Фото',
        dataIndex: 'macroscope_face_id',
        key: 'macroscope_face_id',
        width: 100,
        render: (val) => <Avatar src={"https://4b1ee103-c4f7-4f1b-af2f-fade32f113d3.selstorage.ru/photo_2024-03-16_11-01-04.jpg"} size={64} />
    },
    {
        title: 'ID',
        dataIndex: 'macroscope_face_id',
        key: 'macroscope_face_id',
        width: 100,
        responsive: ['md'],
    },
    {
        title: 'Полное имя',
        width: 150,
        dataIndex: 'full_name',
        key: 'full_name',
    },
    {
        title: 'Идентифицирован',
        key: 'is_identified',
        dataIndex: 'is_identified',
        width: 170,
        render: (val) => <Tag color={val ? 'green' : 'red'}>{val ? 'Да' : 'Нет'}</Tag>,
    },
    {
        title: 'Дата создания пропуска',
        dataIndex: 'pass_issue_date',
        key: 'pass_issue_date',
        width: 200,
        render: (val) => new Date(val).toLocaleDateString("ru", dateOptions),

    },
    {
        title: 'Срок действия пропуска',
        dataIndex: 'pass_expiration_date',
        key: 'pass_expiration_date',
        width: 200,
        render: (val) => new Date(val).toLocaleDateString("ru",dateOptions),
    },
    {
        title: 'Дата обнаружения',
        dataIndex: 'detection_date',
        key: 'detection_date',
        width: 200,
        render: (val) => new Date(val).toLocaleDateString("ru", dateOptions),
    },
]



export const Logs = ({ className }: LogsProps) => {
    const [data, setData] = useState<LogSchema[]>([])
    const tableRef = useRef(null)
    const [showScrollBtn, setShowScrollBtn] = useState(false)
    const socket = useRef<WebSocket>()
    useEffect(() => {
        // $api.get<LogSchema[]>('/logs').then((res) => {
        //     setData(res.data)
        //     setShowScrollBtn(true)
        // })
        socket.current = new WebSocket('ws://localhost:8080/')
        socket.current.onopen = () => {
            console.log(123)
            socket.current.send(JSON.stringify({type: 'read', path: 'logs'}));
        }
        socket.current.onmessage = (event: MessageEvent) => {
            const message = JSON.parse(event.data)
            console.log(message.data)
            setData([...data, ...message.data])
            const tableBody = document.querySelector('.ant-table-body')
            console.log(tableBody)
            tableBody.scrollTo({ top: tableBody.scrollHeight, behavior: 'smooth' })
        }
        socket.current.onclose = () => {
            console.log(321)
        }
        socket.current.onerror = () => {
            console.log("error")
        }
        return () => {
            socket.current?.close()
        }
    }, [])
    const handleClick = () => {
        const tableBody = document.querySelector('.ant-table-body')
        tableBody.scrollTo({ top: tableBody.scrollHeight, behavior: 'smooth' })
    }

    const handleScroll: TableProps<LogSchema>['onScroll'] = (e) => {
        // @ts-ignore
        const { scrollTop, scrollHeight, clientHeight } = e.target
        if (scrollHeight - scrollTop === clientHeight) {
            console.log(123)
            setShowScrollBtn(false)
        } else {
            setShowScrollBtn(true)
        }
    }
    return (
        <div style={{position: 'relative'}}>
            <Table
                columns={columns}
                pagination={false}
                dataSource={data}
                rowClassName={cls.row}
                ref={tableRef}
                scroll={{ y: 500 , x: '100%'}}
                className={cls.table}
                onScroll={handleScroll}
            />
            {showScrollBtn && <Button type='primary' size='large' shape='circle' icon={<ArrowDownOutlined />} className={cls.scrollBtn} onClick={() => handleClick()}></Button>}
        </div>
    );
}

